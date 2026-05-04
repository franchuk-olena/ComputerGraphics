#include <fstream>
#include <iostream>
#include <sstream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "shader_utils.h"
#include "texture.h"

int main(void)
{
    GLFWwindow* window;

    if (!glfwInit())
        return -1;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    window = glfwCreateWindow(640, 480, "Hello World", NULL, NULL);
    if (!window)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    glClearColor(1.0, 1.0, 1.0, 1.0);

    std::string vertexShaderName = "res/shaders/rect.vert";
    std::string fragmentShaderName = "res/shaders/rect.frag";
    GLuint shaderProgram = createProgram(
        vertexShaderName,
        fragmentShaderName);

    GLint texture_loc = glGetUniformLocation(shaderProgram, "uTexture");
    GLint offsetLoc   = glGetUniformLocation(shaderProgram, "uOffset");

    float vertices[] = {
        // Позиції (x, y)     // UV (u, v) - ТУТ МИ МІНЯЄМО 0.0 та 1.0 місцями для Y
        -0.5f, -0.5f,         0.0f, 1.0f,  // було 0.0, стало 1.0
         0.5f, -0.5f,         1.0f, 1.0f,  // було 0.0, стало 1.0
         0.5f,  0.5f,         1.0f, 0.0f,  // було 1.0, стало 0.0
        -0.5f,  0.5f,         0.0f, 0.0f   // було 1.0, стало 0.0
    };

    unsigned int indices[] = {
        0, 1, 2,
        0, 2, 3
    };

    GLuint VBO, EBO, VAO;

    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);
    glGenVertexArrays(1, &VAO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    GLuint posAttrib = glGetAttribLocation(shaderProgram, "aPos");
    glVertexAttribPointer(posAttrib, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(posAttrib);

    GLuint uvAttrib = glGetAttribLocation(shaderProgram, "aUV");
    glVertexAttribPointer(uvAttrib, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void*)(2 * sizeof(float)));
    glEnableVertexAttribArray(uvAttrib);

    glBindVertexArray(0);

    unsigned int texture1 = loadTexture("res/textures/cat.jpeg");
    unsigned int texture2 = loadTexture("res/textures/duck1.jpeg");
    unsigned int texture3 = loadTexture("res/textures/star1.jpeg");

    while (!glfwWindowShouldClose(window))
    {
        glClear(GL_COLOR_BUFFER_BIT);
        glUseProgram(shaderProgram);

        glActiveTexture(GL_TEXTURE0);
        glUniform1i(texture_loc, 0);

        glBindVertexArray(VAO);

        // 1. Верхній лівий (Кіт)
        glUniform2f(offsetLoc, -0.5f, 0.5f); // x = -0.5 (ліворуч), y = 0.5 (вгору)
        glBindTexture(GL_TEXTURE_2D, texture1);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        // 2. Нижній лівий (Качка)
        glUniform2f(offsetLoc, -0.5f, -0.5f); // x = -0.5 (ліворуч), y = -0.5 (вниз)
        glBindTexture(GL_TEXTURE_2D, texture2);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        // 3. Правий центральний (Зірка)
        glUniform2f(offsetLoc, 0.5f, 0.0f);  // x = 0.5 (праворуч), y = 0.0 (центр по вертикалі)
        glBindTexture(GL_TEXTURE_2D, texture3);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glDeleteBuffers(1, &VBO);
    glDeleteBuffers(1, &EBO);
    glDeleteVertexArrays(1, &VAO);
    glDeleteProgram(shaderProgram);

    glDeleteTextures(1, &texture1);
    glDeleteTextures(1, &texture2);
    glDeleteTextures(1, &texture3);

    glfwTerminate();
    return 0;
}