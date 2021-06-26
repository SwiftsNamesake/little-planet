#version 330
// uniform vec4 colour;

uniform vec2 planet_centre;
uniform float planet_radius;

//out vec4 gl_FragColor;

void main() {
    float distance = length(gl_FragCoord.xy - planet_centre) * 0.003;
    vec4 from_colour = vec4(18.0/255.0, 97.0/255.0, 128.0/255.0, 1.0);
    vec4 to_colour = vec4(0.0, 0.0, 0.0, 1.0);

    if (distance < planet_radius) {
        discard;
    } else {
        gl_FragColor  = vec4(mix(from_colour, to_colour, distance).rgb, distance > 0.4 ? 0.0 : 1.0);
    }
}
