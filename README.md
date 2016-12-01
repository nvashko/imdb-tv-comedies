# imdb

## Installation
- Clone the repo: `git clone https://github.com/nvashko/imdb-tv-comedies.git`
- Install python3 development headers: `brew install python3 ; python3-config --include`
- Setup on the environment: `xcode-select --install ; env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2`
- Set the keys:
    cat << EOF
    [imdb]
    key: api_key_here

    [db]
    server: server_here
    database: db_here
    user: user_here
    password: password_here

    EOF >> lib/config
- Create a virutalenv: `mkvirtualenv -p $(which python3) imdb`
- Install the library dependencies: `pip install -r requirements.txt`

## API
- [google docs](https://docs.google.com/document/d/1w2BsVRDoMtKKd3NHWa_KYVAwhUQvf4msRbPxreJpZhI/edit#)
- http://app.imdb.com/
- http://sg.media-imdb.com/suggests/a/aa.json
