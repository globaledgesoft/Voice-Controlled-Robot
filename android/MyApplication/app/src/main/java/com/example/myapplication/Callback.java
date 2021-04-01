package com.example.myapplication;

/**
 * Callback.java communication interface for Fileclient.java and AudioRecorderActivity.java
 *
 */

public interface Callback {
    void processData(String msg);
}
