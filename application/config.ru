require "rubygems"

require "sinatra"
require "sinatra/twitter-bootstrap"

require "haml"

require "./app"

set :run, false
set :raise_errors, true
 
use Rack::CommonLogger

run Sinatra::Application
