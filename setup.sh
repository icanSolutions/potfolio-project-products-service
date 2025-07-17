# products service setup
echo "Setting up Products service env..."

# Create and activate a python local venv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Creating an .env file for env variables
# Check if .env already exists
if [ -f ".env" ]; then
  echo ".env file already exists. Please back it up or delete it if you want to regenerate."
  exit 1
else
  cp .env.example .env
  echo "✅ .env file created from .env.example"
fi

# Add venv/ to .gitignore if not present
if ! grep -q "^venv/$" .gitignore; then
  echo "venv/" >> .gitignore
  echo "✅ Added 'venv/' to .gitignore"
fi

echo "Products service setup complete!"