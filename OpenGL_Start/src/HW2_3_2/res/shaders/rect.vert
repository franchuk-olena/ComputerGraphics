#version 330 core

layout (location = 0) in vec2 aPos;
layout (location = 1) in vec2 aUV;

out vec2 vTexCoords;

uniform float uTime;

void main()
{
    float angle = uTime;

    mat2 rot = mat2(
    cos(angle), -sin(angle),
    sin(angle),  cos(angle)
    );

    vec2 pos = rot * aPos;

    vTexCoords = vec2(aUV.x, 1.0 - aUV.y);

    gl_Position = vec4(pos, 0.0, 1.0);
}