"use strict";

 angular.module("config", [])

.constant("cfg", {
  "version": "0.0.2",
  "host": "mobay.mybluemix.net",
  "debug": false,
  "ssehost": "mobaysse.mybluemix.net",
  "linkedinOauth": "/mobile/auth/linkedin",
  "pushAppId": "cd4d801a-923b-4e47-beca-174a0b1dbd26",
  "pushAppRoute": "mobay.mybluemix.net",
  "pushAppSecret": "d42d7078a870479f902cec88df4757d4b7955582"
})

;