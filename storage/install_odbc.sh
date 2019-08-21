curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -


#Ubuntu 18.10
curl https://packages.microsoft.com/config/ubuntu/18.10/prod.list > /etc/apt/sources.list.d/mssql-release.list

sudo apt-get update -y
sudo ACCEPT_EULA=Y apt-get install msodbcsql17 -y
# optional: for bcp and sqlcmd
sudo ACCEPT_EULA=Y apt-get install mssql-tools -y
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
# optional: for unixODBC development headers
sudo apt-get install unixodbc-dev -y
