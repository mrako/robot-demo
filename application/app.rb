register Sinatra::Twitter::Bootstrap::Assets

set :haml, format: :html5
 
get "/" do
  haml :index
end

post "/submit" do
  haml :result
end

get "/js-test" do
  haml :"js-test"
end

