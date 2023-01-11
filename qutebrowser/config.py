import catppuccin

# load your autoconfig, use this if the rest of your config is empty!
config.load_autoconfig()

# set the flavour you'd like to use
# valid options are 'mocha', 'macchiato', 'frappe', and 'latte'
catppuccin.setup(c, 'mocha')

# enable the ad blocker
config.set('content.blocking.enabled', True)

# tabs visibility
config.set('tabs.show', 'switching')

# open google instead of ddg
config.set('url.default_page', 'https://google.com')
config.set('url.start_pages', ['https://google.com'])
