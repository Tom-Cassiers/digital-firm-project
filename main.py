from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

# Init database - Zélie


# Helper functions - Axel
# Check credit card validity
def CheckCreditCard(number):
    try:
        last = int(number[-1])
        number = number[:-1][::-1]
        total = last
        for digit in number:
            digit = int(digit)
            if(digit % 2 == 0):
                if(digit*2 <= 9):
                    total += digit*2
                else:
                    total += digit * 2 - 9
        return total % 10 == 0
    except:
        return False

# Conversion between currencies
def convertToEuro():
    return

# Routes
# Create company account - Salma
@app.post("/create-company-account")
async def root(payload: Request):
    body = await payload.json()

    name = body['name']

    return name

# Create customer account - Salma
@app.post("/create-customer-account")
async def root(payload: Request):
    body = await payload.json()

    return

# Create quote - Salma
@app.post("/create-quote")
async def root(payload: Request):
    body = await payload.json()

    return

# Create subscription - Zélie
@app.post("/create-subscription")
async def root(payload: Request):
    body = await payload.json()

    return

# Update subscription - Victor
@app.post("/update-subscription")
async def root(payload: Request):
    body = await payload.json()

    return

# Retrieve pending invoices - Victor
@app.post("/pending-invoices")
async def root(payload: Request):
    body = await payload.json()

    return

# Update invoice (paid/unpaid) - Tom
@app.post("/update-invoice")
async def root(payload: Request):
    body = await payload.json()
    
    return

# Retrieve company's statistics - Tom
@app.post("/company-statistics")
async def root(payload: Request):
    body = await payload.json()
    
    return

# Start server
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
