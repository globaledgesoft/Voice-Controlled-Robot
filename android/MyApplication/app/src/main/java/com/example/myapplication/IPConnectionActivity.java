package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;

import com.google.android.material.textfield.TextInputEditText;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;
import android.widget.Button;
import android.widget.Toast;

/**
 * IPConnectionActivity.java to enter the IP address of the server to  connect to android client.
 */
public class IPConnectionActivity extends AppCompatActivity {

     private  TextInputEditText ipedittext;
     private String ipaddress;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_addidng_ip);
         ipedittext= findViewById(R.id.edit_text);
        Button submit = findViewById(R.id.submit_button);

         submit.setOnClickListener(new View.OnClickListener() {
             @Override
             public void onClick(View v) {
                 ipaddress = ipedittext.getText().toString();
                 if (!ipaddress.isEmpty()) {
                     Intent ipIntent = new Intent(IPConnectionActivity.this, AudioRecordActivity.class);
                     ipIntent.putExtra(String.valueOf(R.string.host_ip_address), ipaddress);
                     startActivity(ipIntent);
                 }else {
                     Toast.makeText(getApplicationContext(),R.string.enter_ip_address,Toast.LENGTH_SHORT).show();
                 }
             }
         });
    }

}