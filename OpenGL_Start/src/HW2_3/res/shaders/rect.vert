#version 330 core

layout (location = 0) in vec2 aPos;
layout (location = 1) in vec2 aUV;

out vec2 vTexCoords;

uniform vec2 uOffset;

void main() {
    vTexCoords = aUV;
    gl_Position = vec4(aPos + uOffset, 0.0, 1.0);
}