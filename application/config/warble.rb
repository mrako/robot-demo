Warbler::Config.new do |config|
  config.autodeploy_dir = "deploy"
  config.jar_name = "ROOT"
  config.dirs = %w(public views)
  config.includes = FileList["app.rb"]
  config.gems += ["sinatra", "sinatra-twitter-bootstrap", "haml"]
  config.gems -= ["rails"]
  config.gem_dependencies = true
  config.features = %w(executable)
end
