package com.example.myapplication;



import android.os.AsyncTask;
import android.os.Build;
import android.util.Log;
import androidx.annotation.RequiresApi;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * FileClient.java is used to send audio data and receive
 * lex response through socket
 *
 */
class FileClient extends AsyncTask<Void, Void, String> {
    private final Socket socket;
    private final DataOutputStream mdos ;
    private final DataInputStream mdis ;
    String filename;
    Callback cb;

    FileClient(Socket msocket, DataOutputStream dos, DataInputStream dis, String mFileName, Callback callback) {
        socket= msocket;
        mdis= dis;
        mdos= dos;
        filename = mFileName;
        this.cb=callback;
    }


    @Override
    protected void onPreExecute() {
        super.onPreExecute();
    }

    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    protected String doInBackground(Void... arg0) {
        String str="";
        try {

            byte[] content = Files.readAllBytes(Paths.get(filename));
            String len = String.valueOf(content.length);

            mdos.writeUTF(len);
            mdos.write(content);

            //read the server response message
            int dis_len = Integer.parseInt(mdis.readLine());

            byte[] data = new byte[dis_len];
            if (dis_len > 0) {
                mdis.readFully(data);
            }
            str = new String(data, StandardCharsets.UTF_8);

        } catch (IOException ioException) {
            ioException.printStackTrace();
        }

        return str;

    }


    @Override
    protected void onPostExecute(String result) {
        cb.processData(result);
        super.onPostExecute(result);
    }


}