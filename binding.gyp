{
  "targets": [
    {
      'target_name': 'ctp-napi',
      'sources': [
        'ctp.cc',
        'Mduser.h',
        'Mduser.cpp',
        'MduserEvent.cpp',
        'MduserCall.cpp',
        'MduserAsync.cpp',
        'Trader.h',
        'Trader.cpp',
        'TraderEvent.cpp',
        'TraderCall.cpp',
        'TraderAsync.cpp',
        'Struct.h',
        'SafeQueue.h'
      ],
      "conditions": [
        ["OS=='linux'", {
          "libraries":["$(CURDIR)/ctpapi/20190305/tradeapi_linux64/thostmduserapi.so", "$(CURDIR)/ctpapi/20190305/tradeapi_linux64/thosttraderapi.so"],
          "include_dirs":["./ctpapi/20190305/tradeapi_linux64", "<!@(node -p \"require('node-addon-api').include\")"]
        }],
        ["OS=='win'", {
          "conditions": [
            ["target_arch=='ia32'", {
              "libraries":["./ctpapi/20190305/tradeapi_windows32/thostmduserapi.lib", "./ctpapi/20190305/tradeapi_windows32/thosttraderapi.lib"],
              "include_dirs":["./ctpapi/20190305/tradeapi_windows32", "<!@(node -p \"require('node-addon-api').include\")"],
              "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
            }, { # target_arch=="x64"
              "libraries":["./ctpapi/20190305/tradeapi_windows64/thostmduserapi.lib", "./ctpapi/20190305/tradeapi_windows64/thosttraderapi.lib"],
              "include_dirs":["./ctpapi/20190305/tradeapi_windows64", "<!@(node -p \"require('node-addon-api').include\")"]
            }]
          ]
        }]
      ],
      "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
      "defines": [ "NAPI_CPP_EXCEPTIONS" ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "msvs_settings": {
        "VCCLCompilerTool": { "ExceptionHandling": 1 },
      },
      "xcode_settings": {
        "CLANG_CXX_LIBRARY": "libc++",
        "MACOSX_DEPLOYMENT_TARGET": "10.7",
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
      },
    }
  ]
}