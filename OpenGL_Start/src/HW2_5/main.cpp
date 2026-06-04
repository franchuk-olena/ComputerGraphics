#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "shader_utils.h"

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#include <vector>

struct Cube {
    glm::vec3 position;
    float scale;
    float rotationAngle;
    float rotationSpeed;
    bool isActive;
    glm::vec3 color;
};

glm::vec3 cameraPos = glm::vec3(2.0f, 0.0f, 5.0f);
glm::vec3 cameraFront = glm::vec3(-0.4f, 0.0f, -1.0f);
glm::vec3 cameraUp = glm::vec3(0.0f, 1.0f, 0.0f);

float lastX = 400, lastY = 300;
bool firstMouse = true;
float yaw = -90.0f;
float pitch = 0.0f;
float mouseSensitivity = 0.1f;
float cameraSpeed = 3.0f;

int activeCubeIndex = -1;
bool useStencil = true;

void framebufferSizeCallback(GLFWwindow* window, int width, int height) {
    glViewport(0, 0, width, height);
}

void mouseCallback(GLFWwindow* window, double xpos, double ypos) {
    if (firstMouse) {
        lastX = xpos;
        lastY = ypos;
        firstMouse = false;
    }

    float xoffset = xpos - lastX;
    float yoffset = lastY - ypos;
    lastX = xpos;
    lastY = ypos;

    xoffset *= mouseSensitivity;
    yoffset *= mouseSensitivity;

    yaw += xoffset;
    pitch += yoffset;

    if (pitch > 89.0f) pitch = 89.0f;
    if (pitch < -89.0f) pitch = -89.0f;

    glm::vec3 front;
    front.x = cos(glm::radians(yaw)) * cos(glm::radians(pitch));
    front.y = sin(glm::radians(pitch));
    front.z = sin(glm::radians(yaw)) * cos(glm::radians(pitch));
    cameraFront = glm::normalize(front);
}

void keyCallback(GLFWwindow* window, int key, int scancode, int action, int mods) {
    // Вибір активного куба клавішами 1, 2, 3
    if (action == GLFW_PRESS) {
        if (key == GLFW_KEY_1) activeCubeIndex = 0;
        if (key == GLFW_KEY_2) activeCubeIndex = 1;
        if (key == GLFW_KEY_3) activeCubeIndex = 2;
    }
}

int main(void) {
    GLFWwindow* window;

    if (!glfwInit())
        return -1;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    window = glfwCreateWindow(1000, 800, "Cubes", NULL, NULL);
    if (!window) {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    glfwSetFramebufferSizeCallback(window, framebufferSizeCallback);
    glfwSetCursorPosCallback(window, mouseCallback);
    glfwSetKeyCallback(window, keyCallback);
    glfwSetInputMode(window, GLFW_CURSOR, GLFW_CURSOR_DISABLED);

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_STENCIL_TEST);
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE);
    glStencilFunc(GL_ALWAYS, 1, 0xFF);

    glEnable(GL_CULL_FACE);
    glCullFace(GL_BACK);

    glClearColor(0.1f, 0.1f, 0.15f, 1.0f);

    std::string vertexShaderName = "res/shaders/cube.vert";
    std::string fragmentShaderName = "res/shaders/cube.frag";
    GLuint mainProgram = createProgram(vertexShaderName, fragmentShaderName);

    std::string outlineVertexShader = "res/shaders/outline.vert";
    std::string outlineFragmentShader = "res/shaders/outline.frag";
    GLuint outlineProgram = createProgram(outlineVertexShader, outlineFragmentShader);

    if (mainProgram == 0 || outlineProgram == 0) {
        std::cerr << "Failed to create shader programs" << std::endl;
        glfwTerminate();
        return -1;
    }

    float vertices[] = {
        // Позиції (x,y,z)        // Кольори (r,g,b)        // Текстурні координати
        // Передня грань (червона)
        -0.5f, -0.5f,  0.5f,       1.0f, 0.0f, 0.0f,       0.0f, 0.0f,
         0.5f, -0.5f,  0.5f,       1.0f, 0.0f, 0.0f,       1.0f, 0.0f,
         0.5f,  0.5f,  0.5f,       1.0f, 0.0f, 0.0f,       1.0f, 1.0f,
        -0.5f,  0.5f,  0.5f,       1.0f, 0.0f, 0.0f,       0.0f, 1.0f,

        // Задня грань (зелена)
        -0.5f, -0.5f, -0.5f,       0.0f, 1.0f, 0.0f,       0.0f, 0.0f,
         0.5f, -0.5f, -0.5f,       0.0f, 1.0f, 0.0f,       1.0f, 0.0f,
         0.5f,  0.5f, -0.5f,       0.0f, 1.0f, 0.0f,       1.0f, 1.0f,
        -0.5f,  0.5f, -0.5f,       0.0f, 1.0f, 0.0f,       0.0f, 1.0f,

        // Права грань (синя)
         0.5f, -0.5f,  0.5f,       0.0f, 0.0f, 1.0f,       0.0f, 0.0f,
         0.5f, -0.5f, -0.5f,       0.0f, 0.0f, 1.0f,       1.0f, 0.0f,
         0.5f,  0.5f, -0.5f,       0.0f, 0.0f, 1.0f,       1.0f, 1.0f,
         0.5f,  0.5f,  0.5f,       0.0f, 0.0f, 1.0f,       0.0f, 1.0f,

        // Ліва грань (жовта)
        -0.5f, -0.5f,  0.5f,       1.0f, 1.0f, 0.0f,       0.0f, 0.0f,
        -0.5f, -0.5f, -0.5f,       1.0f, 1.0f, 0.0f,       1.0f, 0.0f,
        -0.5f,  0.5f, -0.5f,       1.0f, 1.0f, 0.0f,       1.0f, 1.0f,
        -0.5f,  0.5f,  0.5f,       1.0f, 1.0f, 0.0f,       0.0f, 1.0f,

        // Верхня грань (пурпурна)
        -0.5f,  0.5f,  0.5f,       1.0f, 0.0f, 1.0f,       0.0f, 0.0f,
         0.5f,  0.5f,  0.5f,       1.0f, 0.0f, 1.0f,       1.0f, 0.0f,
         0.5f,  0.5f, -0.5f,       1.0f, 0.0f, 1.0f,       1.0f, 1.0f,
        -0.5f,  0.5f, -0.5f,       1.0f, 0.0f, 1.0f,       0.0f, 1.0f,

        // Нижня грань (бірюзова)
        -0.5f, -0.5f,  0.5f,       0.0f, 1.0f, 1.0f,       0.0f, 0.0f,
         0.5f, -0.5f,  0.5f,       0.0f, 1.0f, 1.0f,       1.0f, 0.0f,
         0.5f, -0.5f, -0.5f,       0.0f, 1.0f, 1.0f,       1.0f, 1.0f,
        -0.5f, -0.5f, -0.5f,       0.0f, 1.0f, 1.0f,       0.0f, 1.0f
    };

    unsigned int indices[] = {
        0, 1, 2,  2, 3, 0,       // передня
        4, 6, 5,  6, 4, 7,       // задня
        8, 9,10, 10,11, 8,       // ліва
       12,14,13, 14,12,15,       // права
       16,17,18, 18,19,16,       // нижня
       20,22,21, 22,20,23        // верхня
    };


    GLuint VAO, VBO, EBO;
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(3 * sizeof(float)));
    glEnableVertexAttribArray(1);

    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 8 * sizeof(float), (void*)(6 * sizeof(float)));
    glEnableVertexAttribArray(2);

    glBindVertexArray(0);


    std::vector<Cube> cubes = {
        {glm::vec3(-2.0f, -1.0f, 0.0f), 1.0f, 0.0f, 1.0f, false, glm::vec3(1.0f, 0.2f, 0.2f)},
        {glm::vec3(0.0f, 0.5f, -1.0f), 0.8f, 0.0f, 1.2f, false, glm::vec3(0.2f, 1.0f, 0.2f)},
        {glm::vec3(2.0f, 1.0f, -2.0f), 0.6f, 0.0f, 0.8f, false, glm::vec3(0.2f, 0.2f, 1.0f)}
    };

    GLint modelLoc = glGetUniformLocation(mainProgram, "model");
    GLint viewLoc = glGetUniformLocation(mainProgram, "view");
    GLint projLoc = glGetUniformLocation(mainProgram, "projection");

    GLint outlineModelLoc = glGetUniformLocation(outlineProgram, "model");
    GLint outlineViewLoc = glGetUniformLocation(outlineProgram, "view");
    GLint outlineProjLoc = glGetUniformLocation(outlineProgram, "projection");
    GLint outlineColorLoc = glGetUniformLocation(outlineProgram, "outlineColor");

    glm::mat4 projection = glm::perspective(glm::radians(45.0f), 800.0f / 600.0f, 0.1f, 100.0f);

    double lastTime = glfwGetTime();
    double lastFrameTime = lastTime;

    while (!glfwWindowShouldClose(window)) {
        double currentTime = glfwGetTime();
        float deltaTime = (float)(currentTime - lastFrameTime);
        lastFrameTime = currentTime;

        if (deltaTime > 0.1f) deltaTime = 0.1f;

        if (glfwGetKey(window, GLFW_KEY_W) == GLFW_PRESS)
            cameraPos += cameraSpeed * deltaTime * cameraFront;
        if (glfwGetKey(window, GLFW_KEY_S) == GLFW_PRESS)
            cameraPos -= cameraSpeed * deltaTime * cameraFront;
        if (glfwGetKey(window, GLFW_KEY_A) == GLFW_PRESS)
            cameraPos -= glm::normalize(glm::cross(cameraFront, cameraUp)) * cameraSpeed * deltaTime;
        if (glfwGetKey(window, GLFW_KEY_D) == GLFW_PRESS)
            cameraPos += glm::normalize(glm::cross(cameraFront, cameraUp)) * cameraSpeed * deltaTime;

        for (int i = 0; i < cubes.size(); i++) {
            cubes[i].isActive = (i == activeCubeIndex);

            if (cubes[i].isActive) {
                cubes[i].rotationAngle += cubes[i].rotationSpeed * 90.0f * deltaTime;
                if (cubes[i].rotationAngle >= 360.0f) cubes[i].rotationAngle -= 360.0f;
            }
        }

        glStencilMask(0xFF);
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT);

        glm::mat4 view = glm::lookAt(cameraPos, cameraPos + cameraFront, cameraUp);

        glUseProgram(mainProgram);
        glUniformMatrix4fv(viewLoc, 1, GL_FALSE, glm::value_ptr(view));
        glUniformMatrix4fv(projLoc, 1, GL_FALSE, glm::value_ptr(projection));

        glBindVertexArray(VAO);

        for (int i = 0; i < cubes.size(); i++) {
            Cube& cube = cubes[i];

            glStencilFunc(GL_ALWAYS, 1, 0xFF);
            glStencilMask(0xFF);

            glm::mat4 model = glm::mat4(1.0f);
            model = glm::translate(model, cube.position);
            model = glm::scale(model, glm::vec3(cube.scale));

            if (cube.isActive) {
                model = glm::rotate(model, glm::radians(cube.rotationAngle), glm::vec3(1.0f, 1.0f, 0.0f));
                model = glm::rotate(model, glm::radians(cube.rotationAngle), glm::vec3(0.0f, 1.0f, 0.0f));
            }

            glUniformMatrix4fv(modelLoc, 1, GL_FALSE, glm::value_ptr(model));
            glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, 0);
        }

        if (activeCubeIndex >= 0 && activeCubeIndex < cubes.size() && useStencil) {
            glDisable(GL_DEPTH_TEST);
            glStencilFunc(GL_NOTEQUAL, 1, 0xFF);
            glStencilMask(0x00);

            glUseProgram(outlineProgram);
            glUniformMatrix4fv(outlineViewLoc, 1, GL_FALSE, glm::value_ptr(view));
            glUniformMatrix4fv(outlineProjLoc, 1, GL_FALSE, glm::value_ptr(projection));

            Cube& activeCube = cubes[activeCubeIndex];

            glm::mat4 model = glm::mat4(1.0f);
            model = glm::translate(model, activeCube.position);
            model = glm::scale(model, glm::vec3(activeCube.scale * 1.08f));

            if (activeCube.isActive) {
                model = glm::rotate(model, glm::radians(activeCube.rotationAngle), glm::vec3(1.0f, 1.0f, 0.0f));
                model = glm::rotate(model, glm::radians(activeCube.rotationAngle), glm::vec3(0.0f, 1.0f, 0.0f));
            }

            glUniformMatrix4fv(outlineModelLoc, 1, GL_FALSE, glm::value_ptr(model));
            glUniform3fv(outlineColorLoc, 1, glm::value_ptr(activeCube.color));

            glDrawElements(GL_TRIANGLES, 36, GL_UNSIGNED_INT, 0);

            glStencilMask(0xFF);
            glStencilFunc(GL_ALWAYS, 0, 0xFF);
            glEnable(GL_DEPTH_TEST);
        }

        glfwSwapBuffers(window);
        glfwPollEvents();

        if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
            glfwSetWindowShouldClose(window, true);
    }

    glDeleteBuffers(1, &VBO);
    glDeleteBuffers(1, &EBO);
    glDeleteVertexArrays(1, &VAO);
    glDeleteProgram(mainProgram);
    glDeleteProgram(outlineProgram);
    glfwTerminate();
    return 0;
}