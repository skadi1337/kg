#include <glad/glad.h>
#include <GLFW/glfw3.h>

#include <imgui/imgui.h>
#include <imgui/imgui_impl_glfw.h>
#include <imgui/imgui_impl_opengl3.h>

#include <math.h>
#include <iostream>
#include <algorithm>

#define pi 3.14159265359f

void framebuffer_size_callback(GLFWwindow* window, int width, int height)
{
    glViewport(0, 0, width, height);
}


void processInput(GLFWwindow* window)
{
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, true);
}


void rgb_to_cmyk(float* rgb, float* cmyk)
{
    float r = rgb[0] / 255.0f;
    float g = rgb[1] / 255.0f;
    float b = rgb[2] / 255.0f;

    if (r + g + b == 0)
    {
        cmyk[3] = 1;
        cmyk[0] = cmyk[1] = cmyk[2] = 0;
        return;
    }

    cmyk[3] = 1.0f - std::max(r, std::max(g, b));
    auto& k = cmyk[3];


    cmyk[0] = (1.0f - r - k) / (1.0f - k);
    cmyk[1] = (1.0f - g - k) / (1.0f - k);
    cmyk[2] = (1.0f - b - k) / (1.0f - k);

}

void cmyk_to_rgb(float* cmyk, float* rgb)
{
    rgb[0] = (1.0f - cmyk[0]) * (1.0f - cmyk[3]) * 255.0f;
    rgb[1] = (1.0f - cmyk[1]) * (1.0f - cmyk[3]) * 255.0f;
    rgb[2] = (1.0f - cmyk[2]) * (1.0f - cmyk[3]) * 255.0f;
}

void hsl_to_rgb(float* hsl, float* rgb)
{
    auto h = hsl[0];
    if (h == 360)
    {
        h = 0;
    }
    auto& s = hsl[1];
    auto& l = hsl[2];


    float z = (h / 60.0f);

    float c = (1.0f - std::abs(2.0f * l - 1.0f)) * s;
    float x = c * (1.0f - (float)std::abs((fmod(z, 2)) - 1.0f));
    float m = l - (c / 2.0f);

    float r = 0, g = 0, b = 0;
    if (z <= 1)
    {
        r = c;
        g = x;
        b = 0;
    }
    else if (z <= 2)
    {
        r = x;
        g = c;
        b = 0;
    }
    else if (z <= 3)
    {
        r = 0;
        g = c;
        b = x;
    }
    else if (z <= 4)
    {
        r = 0;
        g = x;
        b = c;
    }
    else if (z <= 5)
    {
        r = x;
        g = 0;
        b = c;
    }
    else if (z <= 6)
    {
        r = c;
        g = 0;
        b = x;
    }


    rgb[0] = (r + m) * 255.0f;
    rgb[1] = (g + m) * 255.0f;
    rgb[2] = (b + m) * 255.0f;
}

void rgb_to_hsl(float* rgb, float* hsl)
{
    float r = rgb[0];
    float g = rgb[1];
    float b = rgb[2];

    float cmax = std::max(r, std::max(g, b));
    float cmin = std::min(r, std::min(g, b));
    float delt = (cmax - cmin) / 255.0f;

    auto& h = hsl[0];
    auto& s = hsl[1];
    auto& l = hsl[2];

    l = (cmax + cmin) / 510.0f;

    if (l == 0)
    {
        s = 0;
    }
    else
    {
        s = delt / (1 - std::abs(2.0f * l - 1));
        s = (s == s) ? s : 0;
    }

    if (g >= b)
    {
        h = (float)std::acos((r - 0.5 * g - 0.5 * b) / (std::sqrt(r * r + g * g + b * b - r * g - r * b - g * b))) * 180.0f / pi;
    }

    if (b > g)
    {
        h = 360.0f - (float)std::acos((r - 0.5 * g - 0.5 * b) / (std::sqrt(r * r + g * g + b * b - r * g - r * b - g * b))) * 180 / pi;
    }

    h = (h == h) ? h : 0;

}



int main()
{
    glfwInit();
    const char* glsl_version = "#version 130";
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    //glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);


    GLFWwindow* window = glfwCreateWindow(1200, 800, "Colors", NULL, NULL);
    if (window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);


    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
    {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }


    glViewport(0, 0, 1200, 800);
    glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);


    ImGui::CreateContext();
    ImGui::StyleColorsDark();
    ImGui_ImplGlfw_InitForOpenGL(window, true);
    ImGui_ImplOpenGL3_Init(glsl_version);


    ImVec4 clear_color = ImVec4(0.2f, 0.3f, 0.3f, 1.0f);
    ImVec4 rgb_color = ImVec4(51.0f, 76.5f, 76.5f, 1.0f);
    ImVec4 cmyk_color = ImVec4(0.2f, 0.3f, 0.3f, 1.0f);
    ImVec4 hsl_color = ImVec4(180.0f, 0.2f, 0.25f, 1.0f);


    while (!glfwWindowShouldClose(window))
    {
        processInput(window);

        glClearColor(clear_color.x, clear_color.y, clear_color.z, clear_color.w);
        glClear(GL_COLOR_BUFFER_BIT);

        
        ImGui_ImplOpenGL3_NewFrame();
        ImGui_ImplGlfw_NewFrame();
        ImGui::NewFrame();
        {
            ImGui::Begin("Color");

            if (ImGui::ColorPicker4("##picker", (float*)&clear_color, ImGuiColorEditFlags_NoInputs | ImGuiColorEditFlags_NoSidePreview | ImGuiColorEditFlags_NoSmallPreview))
            {
                if (clear_color.x > 255)
                    clear_color.x = 255;
                if (clear_color.y > 255)
                    clear_color.y = 255;
                if (clear_color.z > 255)
                    clear_color.z = 255;

                if (clear_color.x < 0)
                    clear_color.x = 0;
                if (clear_color.y < 0)
                    clear_color.y = 0;
                if (clear_color.z < 0)
                    clear_color.z = 0;



                rgb_color.x = clear_color.x * 255.0f;
                rgb_color.y = clear_color.y * 255.0f;
                rgb_color.z = clear_color.z * 255.0f;
                rgb_to_cmyk((float*)&rgb_color, (float*)&cmyk_color);
                rgb_to_hsl((float*)&rgb_color, (float*)&hsl_color);
            }

            ImGui::Text("RGB*");
            ImGui::SameLine();
            if (ImGui::DragFloat3("##RGB*", (float*)&clear_color, 0.01f, 0.0f, 1.0f))
            {
                if (clear_color.x > 255)
                    clear_color.x = 255;
                if (clear_color.y > 255)
                    clear_color.y = 255;
                if (clear_color.z > 255)
                    clear_color.z = 255;

                if (clear_color.x < 0)
                    clear_color.x = 0;
                if (clear_color.y < 0)
                    clear_color.y = 0;
                if (clear_color.z < 0)
                    clear_color.z = 0;

                rgb_color.x = clear_color.x * 255.0f;
                rgb_color.y = clear_color.y * 255.0f;
                rgb_color.z = clear_color.z * 255.0f;
                rgb_to_cmyk((float*)&rgb_color, (float*)&cmyk_color);
                rgb_to_hsl((float*)&rgb_color, (float*)&hsl_color);
            }

            ImGui::Text("RGB ");
            ImGui::SameLine();
            if (ImGui::DragFloat3("##RGB", (float*)&rgb_color, 1.0f, 0.0f, 255.0f, "%.f"))
            {
                if (rgb_color.x > 255)
                    rgb_color.x = 255;
                if (rgb_color.y > 255)
                    rgb_color.y = 255;
                if (rgb_color.z > 255)
                    rgb_color.z = 255;

                if (rgb_color.x < 0)
                    rgb_color.x = 0;
                if (rgb_color.y < 0)
                    rgb_color.y = 0;
                if (rgb_color.z < 0)
                    rgb_color.z = 0;

                rgb_to_cmyk((float*)&rgb_color, (float*)&cmyk_color);
                rgb_to_hsl((float*)&rgb_color, (float*)&hsl_color);
            }

            ImGui::Text("CMYK");
            ImGui::SameLine();
            if (ImGui::DragFloat4("##CMYK", (float*)&cmyk_color, 0.01f, 0.0f, 1.0f))
            {
                if (cmyk_color.x > 1)
                    cmyk_color.x = 1;
                if (cmyk_color.y > 1)
                    cmyk_color.y = 1;
                if (cmyk_color.z > 1)
                    cmyk_color.z = 1;
                if (cmyk_color.w > 1)
                    cmyk_color.w = 1;

                if (cmyk_color.x < 0)
                    cmyk_color.x = 0;
                if (cmyk_color.y < 0)
                    cmyk_color.y = 0;
                if (cmyk_color.z < 0)
                    cmyk_color.z = 0;
                if (cmyk_color.w < 0)
                    cmyk_color.w = 1;

                cmyk_to_rgb((float*)&cmyk_color, (float*)&rgb_color);
                rgb_to_hsl((float*)&rgb_color, (float*)&hsl_color);
            }

            ImGui::Text("HSL ");
            ImGui::SameLine();
            if (ImGui::DragFloat("##HLS_H", &hsl_color.x, 1.0f, 0.0f, 360.0f, "%.f"))
            {
                if (hsl_color.x > 360)
                    hsl_color.x = 360;
                if (hsl_color.x < 0)
                    hsl_color.x = 0;

                hsl_to_rgb((float*)&hsl_color, (float*)&rgb_color);
                rgb_to_cmyk((float*)&rgb_color, (float*)&cmyk_color);
            }

            if (ImGui::DragFloat2("##HLS_SL", (float*)&hsl_color.y, 0.01f, 0.0f, 1.0f))
            {
                if (hsl_color.y > 1)
                    hsl_color.y = 1;
                if (hsl_color.y < 0)
                    hsl_color.y = 0;
                if (hsl_color.z > 1)
                    hsl_color.z = 1;
                if (hsl_color.z < 0)
                    hsl_color.z = 0;

                hsl_to_rgb((float*)&hsl_color, (float*)&rgb_color);
                rgb_to_cmyk((float*)&rgb_color, (float*)&cmyk_color);
            }

            ImGui::End();
        }

        ImGui::Render();
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());


        clear_color.x = rgb_color.x / 255.0f;
        clear_color.y = rgb_color.y / 255.0f;
        clear_color.z = rgb_color.z / 255.0f;


        glfwSwapBuffers(window);
        glfwPollEvents();
    }


    glfwTerminate();
    return 0;
}