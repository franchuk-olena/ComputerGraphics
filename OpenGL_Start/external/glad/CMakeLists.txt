
file(
        GLOB_RECURSE GLAD_SRC
        *.h
        *.cpp
        *.c
)

#message("GlAD SOURCES: " ${GLAD_SRC})

add_library(glad STATIC ${GLAD_SRC})
target_include_directories(glad PUBLIC include)