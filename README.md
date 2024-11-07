# AI Chat System API

This project is a Django-based REST API for an AI chat system, enabling users to register, log in, and interact with an AI chatbot. Each message sent to the chatbot deducts tokens from the user's balance, and users can also check their remaining tokens.

## Features

- **User Registration**: Allows new users to register with a unique username and password. Each user starts with 4000 tokens.
- **User Login**: Enables users to log in and obtain an authentication token required for subsequent API requests.
- **Chat with AI**: Users can send messages to the chatbot and receive responses. Each message deducts 100 tokens.
- **Check Token Balance**: Users can check the number of remaining tokens in their account.

## Technologies

- Django and Django REST Framework (DRF)
- SQLite (default database for simplicity, can be changed)
- Token-based authentication

## Models

### User Model
- `username`: Unique identifier for each user.
- `password`: Stores a hashed version of the user's password.
- `tokens`: Tracks the user's available tokens, initialized to 4000.

### Chat Model
- `user`: Foreign key relationship to the User model.
- `message`: Stores the message sent by the user.
- `response`: Stores the AI's response to the user message (dummy value).
- `timestamp`: Records the time of each chat message.

## API Endpoints

1. **User Registration**
   - **URL**: `/api/register/`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "username": "unique_username",
       "password": "user_password"
     }
     ```
   - **Response**:
     - **Success**: `201 Created`, with a message indicating successful registration.
     - **Failure**: Error message if username is already taken or validation fails.

2. **User Login**
   - **URL**: `/api/login/`
   - **Method**: `POST`
   - **Request Body**:
     ```json
     {
       "username": "username",
       "password": "password"
     }
     ```
   - **Response**:
     - **Success**: `200 OK` with an authentication token.
     - **Failure**: `401 Unauthorized` with an error message for incorrect credentials.

3. **Chat with AI**
   - **URL**: `/api/chat/`
   - **Method**: `POST`
   - **Headers**: `Authorization: Token <user_token>`
   - **Request Body**:
     ```json
     {
       "message": "User's question"
     }
     ```
   - **Response**:
     - **Success**: `200 OK` with AI response and deducted token count.
     - **Failure**:
       - `403 Forbidden` if token is missing or invalid.
       - `402 Payment Required` if tokens are insufficient.

4. **Check Token Balance**
   - **URL**: `/api/balance/`
   - **Method**: `GET`
   - **Headers**: `Authorization: Token <user_token>`
   - **Response**:
     - **Success**: `200 OK` with current token balance.
     - **Failure**: `403 Forbidden` if token is missing or invalid.

## Installation and Setup

1. Clone the repository
   ```bash
   git clone https://github.com/Nishantrde/AI_Chat_Bot
   cd ai-chat-system

2. Create a virtual environment and activate it
   ```bash
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Run migrations
   ```bash
   python manage.py migrate

5. Start the development server
   ```bash
   python manage.py runserver

5. Start the development server
   ```bash
   http://127.0.0.1:8000/api/

# Example Usage

Here’s how to interact with the API endpoints.

  ## Registration
      
        curl -X POST http://127.0.0.1:8000/api/register/ -H "Content-Type: application/json" -d "{\"username\":\"name\", \"password\":\"pw@123\"}"

  ## Login
      
      curl -X POST http://127.0.0.1:8000/api/login/ -H "Content-Type: application/json" -d "{\"username\":\"name\", \"password\":\"pw@123\"}"

  ## Chat with AI
      curl -X POST http://127.0.0.1:8000/api/chat/ -H "Content-Type: application/json" -H "Authorization: Token <token>" -d "{\"message\":\"hello\"}"

  ## Check balance
   
    curl -X GET http://127.0.0.1:8000/api/balance/ -H "Content-Type: application/json" -H "Authorization: Token <token>" 

  # Smaples
  ## Starting the server

![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731002412/Screenshot_2024-11-07_095350_lybjpr.png)

  ## Registration api

   ![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731002412/Screenshot_2024-11-07_095540_wfa2s6.png)

  ## Login api

   ![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731002760/Screenshot_2024-11-07_100543_xi96xv.png)
  
  ## Chat api

   ![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731002412/Screenshot_2024-11-07_095813_l80ydj.png)

  ## Balance api

   ![App Screenshot](https://res.cloudinary.com/dwfdyavop/image/upload/v1731002412/Screenshot_2024-11-07_095937_sdhhdp.png)
