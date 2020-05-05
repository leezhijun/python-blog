module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    "generator-star-spacing": "off",
    "no-tabs":"off",
    "no-unused-vars":"off",
    "no-irregular-whitespace":"off",
    'semi': 'off',
    'space-before-fun': 'off',
    'comma-dangle': 'off',
    'space-before-function-paren': 'off',
    'indent': 'off',
    'dot-notation': 'off',
    'comma-spacing': 'off',
    'arrow-spacing': 'off',
    'space-infix-ops': 'off',
    'quotes': 'off',
    'keyword-spacing': 'off',
    'camelcase': 'off',
    'curly': 'off',
    'no-mixed-spaces-and-tabs': 'off',
    'no-useless-escape': 'off',
    'no-unreachable': 'off',
    "no-useless-escape": 0//这里设置为0则可通过检查
  }
}
