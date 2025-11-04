mkdir -p data
cd data || exit
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew install wget
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update
    sudo apt-get install -y wget
elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* || "$OSTYPE" == "win32"* ]]; then
    echo "Please install wget manually or use Chocolatey: choco install wget"
    exit 1
else
    echo "Unsupported OS"
    exit 1
fi

wget https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/candy-power-ranking/candy-data.csv
wget https://raw.githubusercontent.com/mansimajithia/ETLProject-Candy-Dataset/refs/heads/master/Resources/transformed_candy_3.csv
