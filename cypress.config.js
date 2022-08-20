"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var cypress_1 = require("cypress");
exports.default = cypress_1.defineConfig({
    e2e: {
        setupNodeEvents: function (on, config) {
            // implement node event listeners here
        },
        "chromeWebSecurity": false,
        "baseUrl": "https://app.quantimo.do",
        "projectId": "1rj181",
        "pageLoadTimeout": 60000,
        "videoCompression": false,
        "videoUploadOnPasses": false,
        "video": true,
        "env": {
            "API_HOST": "app.quantimo.do",
            "OAUTH_APP_HOST": "web.quantimo.do",
            "BUILDER_HOST": "builder.quantimo.do",
            "abort_strategy": true
        },
        "reporter": "cypress-multi-reporters",
        "reporterOptions": {
            "configFile": "cypress/reporterOpts.json"
        },
        "screenshotsFolder": "cypress/reports/assets"
    },
});
