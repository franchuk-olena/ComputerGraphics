#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include "shader_utils.h"
#include "texture.h"

int main()
{
    glfwInit();

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(640, 480, "SPP", NULL, NULL);
    glfwMakeContextCurrent(window);

    gladLoadGLLoader((GLADloadproc)glfwGetProcAddress);

    glClearColor(1,1,1,1);

    std::string vs = "res/shaders/rect.vert";
    std::string fs = "res/shaders/rect.frag";

    GLuint shaderProgram = createProgram(vs, fs);

    GLint timeLoc = glGetUniformLocation(shaderProgram, "uTime");
    GLint texLoc  = glGetUniformLocation(shaderProgram, "uTexture");

    float vertices[] = {
        -0.5f,-0.5f,  0.0f,0.0f,
         0.5f,-0.5f,  1.0f,0.0f,
         0.5f, 0.5f,  1.0f,1.0f,
        -0.5f, 0.5f,  0.0f,1.0f
    };

    unsigned int indices[] = {0,1,2, 0,2,3};

    GLuint VAO,VBO,EBO;

    glGenVertexArrays(1,&VAO);
    glGenBuffers(1,&VBO);
    glGenBuffers(1,&EBO);

    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER,VBO);
    glBufferData(GL_ARRAY_BUFFER,sizeof(vertices),vertices,GL_STATIC_DRAW);

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,sizeof(indices),indices,GL_STATIC_DRAW);

    glVertexAttribPointer(0,2,GL_FLOAT,GL_FALSE,4*sizeof(float),(void*)0);
    glEnableVertexAttribArray(0);

    glVertexAttribPointer(1,2,GL_FLOAT,GL_FALSE,4*sizeof(float),(void*)(2*sizeof(float)));
    glEnableVertexAttribArray(1);

    glBindVertexArray(0);

    unsigned int texture = loadTexture("res/textures/cat.jpeg");

    while (!glfwWindowShouldClose(window))
    {
        glClear(GL_COLOR_BUFFER_BIT);
        glUseProgram(shaderProgram);

        float time = (float)glfwGetTime();

        glUniform1f(timeLoc, time);

        glActiveTexture(GL_TEXTURE0);
        glBindTexture(GL_TEXTURE_2D, texture);
        glUniform1i(texLoc, 0);

        glBindVertexArray(VAO);
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}