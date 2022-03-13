from pydantic import BaseSettings


class Setting(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secrete_key: str
    algorithms: str
    access_token_expiration_time: int

    class Config:
        env_file = ".env"


# the file reading from the disk is normally a very slow procees but once we can read the file from the disk
# then it will be used agian and again
# b/z if we read again and again from the disk it harm over website and also slow the server side response
setting = Setting()
