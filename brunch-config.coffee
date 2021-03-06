exports.config =
  conventions:
    assets: /assets\/.*/

  npm:
    globals:
      $: 'jquery'
      _: 'lodash'
      jQuery: 'jquery'
      Bootstrap: 'bootstrap'
      Tether: 'tether'
      React: 'react'

  sourceMaps: true
  paths:
    # doc: https://github.com/brunch/brunch/blob/master/docs/config.md#paths
    watched: [
      'components'
      'javascript'
      'scss'
      'styles'
      'assets'
    ]
    public: 'static'

  modules:
    addSourceURLs: true
    nameCleaner: (path) ->
      path
        .replace(/^components\//, '')
        .replace(/^javascript\//, '')
        .replace(/\.jsx/, '')
        .replace(/\.js/, '')

  files:
    javascripts:
      joinTo:
        'js/{{project_name}}.js': /^javascript|^components/
        'js/vendor.js': /node_modules/
      order:
        before: [
          'node_modules/popper.js/dist/umd/popper.js'
          'node_modules/jquery/dist/jquery.js'
        ]
        after: [
          'react/index.js'
        ]

    stylesheets:
      joinTo:
        'css/vendor.css': /^scss/
        'css/{{project_name}}.css': /^styles/
      order:
        before: [
          '{{project_name}}.scss'
        ]
        after: [
          '{{project_name}}.styl'
        ]

  overrides:
    production:
      sourceMaps: false
      optimize: true
      plugins: autoReload: enabled: false

  plugins:

#    afterBrunch: [
#      'django-admin collectstatic --no-input'
#    ]

    flowtype:
      warnOnly:  false,
      method:    'status',
      statusDelay: 250

    autoReload:
      enabled: true

    babel:
      babelrc: false
      plugins: ['transform-flow-strip-types']
      presets: ['env', 'react', 'flow', ]
      ignore: [
        /(node_modules|vendor)/
      ]

    coffeescript:
      bare: true

    coffeelint:
      pattern: /.*\.coffee$/
      options:
        max_line_length:
          level: 'ignore'

    postcss:
      processors: [
        require('autoprefixer')({browsers: ['last 2 versions', 'ie >= 9', 'and_chr >= 2.3']})
      ]

    presets:
      env:
        targets:
          browsers: ["last 2 versions", "safari >= 7"]

    react:
      autoIncludeCommentBlock: yes

    sass:
      mode: 'native'
      sourceMapEmbed: true
      debug: 'comments'
      allowCache: true
      options:
        includePaths: [
          'node_modules/bootstrap/scss',
        ]
