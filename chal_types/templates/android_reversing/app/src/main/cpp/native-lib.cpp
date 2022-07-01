#include <jni.h>
#include <string>

static int seq[] = {6, 3, 5, 7, 1, 0, 9, 4, 2, 8};
static char out[sizeof(seq) + 1] = {'\0'};

extern "C" JNIEXPORT jstring

JNICALL
Java_com_mcpshsf_mobile_challenge1_MainActivity_stringFromJNI(
        JNIEnv *env,
        jobject /* this */) {
    std::string hello = "This is the second part: \"_static_\"";
    return env->NewStringUTF(hello.c_str());
}

extern "C" JNIEXPORT void

JNICALL
Java_com_mcpshsf_mobile_challenge1_MainActivity_oneLastThing(
        JNIEnv *env,
     jobject /* this */) {
}
