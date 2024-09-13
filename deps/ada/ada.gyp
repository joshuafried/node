{
  'variables': {
    'v8_enable_i18n_support%': 1,
    'ada_sources': [ '../../ada/src/ada.cpp' ],
  },
  'targets': [
    {
      'target_name': 'ada',
      'type': 'static_library',
      'include_dirs': ['../../ada/include'],
      'direct_dependent_settings': {
        'include_dirs': ['../../ada/include'],
      },
      'sources': [ '<@(ada_sources)' ]
    },
  ]
}
