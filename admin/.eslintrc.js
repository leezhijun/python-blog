module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    "generator-star-spacing": "off",
    "no-tabs":"off",
    "no-unused-vars":"off",
    "no-irregular-whitespace":"off",
    'semi': 'off',
    'space-before-fun': 'off',
    'comma-dangle': 'off',
    'space-before-function-paren': 'off'
  }
}
