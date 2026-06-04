#define _USE_MATH_DEFINES // Для підтримки M_PI на всіх системах
#include <cmath>
#include <iostream>
#include <algorithm>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "shader_utils.h"
#include "texture.h"

#include <glm/glm.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtc/matrix_transform.hpp>

// Виправлена функція перевірки наведення миші (працює і на Retina дисплеях Mac)
bool isMouseOverRectangle(double mouseX, double mouseY, float rectX, float rectY, float rectWidth, float rectHeight, int winWidth, int winHeight) {
    // Переводимо екранні пікселі в NDC координати OpenGL (-1.0 до 1.0)
    float glMouseX = (2.0f * (float)mouseX) / winWidth - 1.0f;
    float glMouseY = 1.0f - (2.0f * (float)mouseY) / winHeight;

    // Перевіряємо, чи потрапляє миша в межі прямокутника
    return (glMouseX >= rectX - rectWidth / 2.0f && glMouseX <= rectX + rectWidth / 2.0f &&
            glMouseY >= rectY - rectHeight / 2.0f && glMouseY <= rectY + rectHeight / 2.0f);
}

int main(void)
{
    GLFWwindow* window;

    if (!glfwInit())
        return -1;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    const int width = 800;
    const int height = 600;

    window = glfwCreateWindow(width, height, "Завдання 2_4 - Олена", NULL, NULL);
    if (!window)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc) glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);

    // Увага! Переконайся, що файли у папці res/shaders називаються саме так:
    std::string vertexShaderName = "/Users/olena/ComputerGraphics/OpenGL_Start/src/HW2_4/res/shaders/outline.vert";
    std::string fragmentShaderName = "/Users/olena/ComputerGraphics/OpenGL_Start/src/HW2_4/res/shaders/rect.frag";
    GLuint program = createProgram(vertexShaderName, fragmentShaderName);

    GLint texture_loc = glGetUniformLocation(program, "uTexture");
    GLint transform_loc = glGetUniformLocation(program, "uTransformation");

    // Координати вершин та текстур
    float vertices[] = {
        -0.25f,  0.25f,     0.0f, 1.0f,
        -0.25f, -0.25f,     0.0f, 0.0f,
         0.25f, -0.25f,     1.0f, 0.0f,

        -0.25f,  0.25f,     0.0f, 1.0f,
         0.25f, -0.25f,     1.0f, 0.0f,
         0.25f,  0.25f,     1.0f, 1.0f
    };

    GLuint VAO, VBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glBindVertexArray(VAO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    GLint posAttribLocation = glGetAttribLocation(program, "aPos");
    GLint textureCoordsAttribLocation = glGetAttribLocation(program, "aUV");

    glVertexAttribPointer(posAttribLocation, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(posAttribLocation);
    glVertexAttribPointer(textureCoordsAttribLocation, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));
    glEnableVertexAttribArray(textureCoordsAttribLocation);
    glBindVertexArray(0);

    // Змінено розширення з .png на .jpg відповідно до твоїх файлів textures - img3.jpg
    GLuint texture1 = loadTexture("/Users/olena/ComputerGraphics/OpenGL_Start/src/HW2_4/res/textures/photo.png");

    // Логіка трансформацій
    float posX = 0.0f;
    float posY = 0.0f;
    float angle = 0.0f;
    bool isHovered = false;

    double mouseX, mouseY;
    float rectWidth = 0.5f;
    float rectHeight = 0.5f;
    float rotationSpeed = 3.0f;

    double lastTime = glfwGetTime();

    while (!glfwWindowShouldClose(window))
    {
        double currentTime = glfwGetTime();
        float deltaTime = (float)(currentTime - lastTime);
        lastTime = currentTime;

        glClear(GL_COLOR_BUFFER_BIT);

        // Рух (Клавіатура)
        float speed = 2.0f * deltaTime;
        if (glfwGetKey(window, GLFW_KEY_LEFT) == GLFW_PRESS)  posX -= speed;
        if (glfwGetKey(window, GLFW_KEY_RIGHT) == GLFW_PRESS) posX += speed;
        if (glfwGetKey(window, GLFW_KEY_UP) == GLFW_PRESS)    posY += speed;
        if (glfwGetKey(window, GLFW_KEY_DOWN) == GLFW_PRESS)  posY -= speed;

        posX = std::max(-0.75f, std::min(0.75f, posX));
        posY = std::max(-0.75f, std::min(0.75f, posY));

        // Отримання координат миші
        glfwGetCursorPos(window, &mouseX, &mouseY);

        // Динамічно отримуємо поточний розмір вікна (запобігає багам на Mac Retina)
        int currentWinWidth, currentWinHeight;
        glfwGetWindowSize(window, &currentWinWidth, &currentWinHeight);

        // Перевірка наведення
        bool currentlyHovered = isMouseOverRectangle(mouseX, mouseY, posX, posY, rectWidth, rectHeight, currentWinWidth, currentWinHeight);

        if (currentlyHovered && !isHovered) {
            glfwSetCursor(window, glfwCreateStandardCursor(GLFW_HAND_CURSOR));
        } else if (!currentlyHovered && isHovered) {
            glfwSetCursor(window, NULL);
        }
        isHovered = currentlyHovered;

        // Якщо миша наведена — обертаємо навколо власного центру
        if (isHovered) {
            angle += rotationSpeed * deltaTime;
            if (angle > 2.0f * (float)M_PI) angle -= 2.0f * (float)M_PI;
        }

        // Матриця uTransformation
        glm::mat4 transform = glm::mat4(1.0f);
        transform = glm::translate(transform, glm::vec3(posX, posY, 0.0f));
        transform = glm::rotate(transform, angle, glm::vec3(0.0f, 0.0f, 1.0f));

        glUseProgram(program);
        glUniformMatrix4fv(transform_loc, 1, GL_FALSE, glm::value_ptr(transform));

        glBindVertexArray(VAO);
        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture1);
        glUniform1i(texture_loc, 0);

        glDrawArrays(GL_TRIANGLES, 0, 6);

        glfwSwapBuffers(window);
        glfwPollEvents();

        if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
            glfwSetWindowShouldClose(window, true);
    }

    glDeleteBuffers(1, &VBO);
    glDeleteVertexArrays(1, &VAO);
    glDeleteProgram(program);
    glDeleteTextures(1, &texture1);
    glfwTerminate();
    return 0;
}