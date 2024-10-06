// init-mongo.js

db = db.getSiblingDB('degressly');

// Optional: If you want to create a user for this database
db.createUser({
    user: "degressly_user",
    pwd: "secure_password", // Replace with your own password
    roles: [
        {
            role: "readWrite",
            db: "degressly"
        }
    ]
});

