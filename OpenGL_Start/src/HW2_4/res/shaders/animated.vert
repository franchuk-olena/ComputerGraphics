#version 330 core

in vec4 aPos;
in vec2 aUV;

out vec2 vTexCoords;

uniform mat4 uTransformation;

void main() {
    vTexCoords = aUV;
    // Множимо матрицю на позицію вершини
    gl_Position = uTransformation * aPos;
}