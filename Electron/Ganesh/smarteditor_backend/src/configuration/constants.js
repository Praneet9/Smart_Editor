const devConfig = {
  MONGO_URL: "mongodb://localhost/smarteditor-dev"
};

const testConfig = {
  MONGO_URL: "mongodb://localhost/smarteditor-test"
};

const prodConfig = {
  MONGO_URL: "mongodb://localhost/smarteditor-prod"
};

const defaultConfig = {
  PORT: process.env.PORT || 3000
};

function envConfig(env) {
  switch (env) {
    case "development":
      return devConfig;
    case "test":
      return testConfig;
    default:
      return prodConfig;
  }
}

export default {
  ...defaultConfig,
  ...envConfig(process.env.NODE_ENV)
};
