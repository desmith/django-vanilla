exports.config =
  npm:
    globals:
      $: 'jquery'
      jQuery: 'jquery'
      _: 'lodash'
      Tether: 'tether'
      Bootstrap: 'bootstrap'
      #React: 'react'
      #ReactDOM: 'react-dom'
      #Router: 'react-router'

  sourceMaps: true
  paths:
    # doc: https://github.com/brunch/brunch/blob/master/docs/config.md#paths
    watched: ['react']
    public: 'static'

  modules:
    addSourceURLs: true
    nameCleaner: (path) ->
      path
        #.replace(/^react\/components\//, '')
        .replace(/^react\//, '')
        .replace(/^components\//, '')
        .replace(/^javascripts\//, '')
        .replace(/\.jsx/, '')
        .replace(/\.js/, '')
#    autoRequire:
#      'js/inews.js': ['inews']

  files:
    javascripts:
      joinTo:
        'js/inews.js': /^react/
        'js/vendor.js': /node_modules/
      order:
        before: [
          'node_modules/jquery/dist/jquery.js'
        ]
        after: [
          'react/index.js'
        ]

    stylesheets:
      joinTo:
        'css/{{project_name}}.css': /^react/
      order:
        before: [
        ]
        after: [
          'inews.styl'
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

    autoReload:
      enabled: true

    babel:
      babelrc: false
      presets: ['env', 'react', 'es2015', 'es2016' ]
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
      options:
        includePaths: [
          'node_modules/bootstrap/scss',
          'node_modules/motion-ui/src'
        ]
