#version 330 core

in vec3 vColor;
in vec2 vUV;
out vec4 FragColor;

uniform sampler2D uTexture;
uniform bool useTexture;

void main() {
    if (useTexture) {
        vec4 texColor = texture(uTexture, vUV);
        FragColor = vec4(vColor, 1.0) * texColor;
    } else {
        FragColor = vec4(vColor, 1.0);
    }
}