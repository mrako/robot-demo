require 'sinatra'

get '/' do
  erb :index
end

post "/submit" do
  erb :result
end

