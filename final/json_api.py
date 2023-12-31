import json

json_data = {
    "Low Carb": {
        "Breakfast": [
                        {
                        "id": 0,
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Low Carb one",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast1.jpg"
                        },
                        { 
                        "id": 1,
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Low Carb two",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 250,
                        "img":"images/breakfast7.jpg"
                        },
                        { 
                        "id": 2,
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Low Carb three",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 300,
                        "img":"images/breakfast4.jpg"
                        }
        ],
        "Lunch": [
                    { 
                    "id": 0,
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Low Carb one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 350,
                    "img":"images/dinner7.jpg"
                    },
                    { 
                    "id": 1,    
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Low Carb two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/lunch4.jpg"
                    },
                    { 
                    "id": 2,
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Low Carb three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/lunch6.jpg"
                    }
        ],
        "Dinner": [
                    { 
                    "id": 0,
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Low Carb one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 320,
                    "img":"images/lunch1.jpg"
                    },
                    { 
                    "id":1,   
                    "the_meal": "Dinner",  
                    "meal_title": "Dinner Low Carb two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 340,
                    "img":"images/lunch2.jpg"
                    },
                    { 
                    "id":2, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Low Carb three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 360,
                    "img":"images/lunch3.jpg"
                    }
        ],
        "Snack": [
                    {
                    "id":0, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Low Carb one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 100,
                    "img":"images/snack1.jpg"
                    },
                    { 
                    "id":1, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Low Carb two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 120,
                    "img":"images/snack4.jpg"
                    },
                    { 
                    "id":2, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Low Carb three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 140,
                    "img":"images/snack6.jpg"
                    }
        ]
    },
    "High Protein": {
        "Breakfast": [
                        {
                        "id":0, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast High Protein one",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast1.jpg"
                        },
                        {
                        "id":1, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast High Protein two",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast5.jpg"
                        },
                        {
                        "id":2, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast High Protein three",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                            ,
                        "calories": 200,
                        "img":"images/breakfast7.jpg"
                        }
        ],
        "Lunch": [
                    {
                    "id":0, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch High Protein one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/dinner4.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch High Protein two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/lunch5.jpg"
                    },
                    { 
                    "id":2, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch High Protein three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/lunch4.jpg"
                    }
        ],
        "Dinner": [
                    { 
                    "id":0, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner High Protein one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/dinner1.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner High Protein two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/dinner5.jpg"
                    },
                    { 
                    "id":2, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner High Protein three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/dinner3.jpg"
                    }
        ],
        "Snack": [
                    { 
                    "id":0, 
                    "the_meal": "Snack",
                    "meal_title": "Snack High Protein one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack2.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Snack",
                    "meal_title": "Snack High Protein two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack3.jpg"
                    },
                    {
                    "id":2, 
                    "the_meal": "Snack",
                    "meal_title": "Snack High Protein three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack4.jpg"
                    }
        ]
    },
    "Vegan": {
        "Breakfast": [
                        {
                        "id":0, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Vegan one",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast2.jpg"
                        },
                        {
                        "id":1, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Vegan two",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast6.jpg"
                        },
                        {
                        "id":2, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Vegan three",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast3.jpg"
                        }
        ],
        "Lunch": [
                    {
                    "id":0, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Vegan one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/lunch1.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Vegan two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 200,
                    "img":"images/dinner3.jpg"
                    },
                    {
                    "id":2, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Vegan three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/dinner4.jpg"
                    }
        ],
        "Dinner": [
                    {
                    "id":0, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Vegan one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/lunch5.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Vegan two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/dinner1.jpg"
                    },
                    {
                    "id":2, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Vegan three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/dinner5.jpg"
                    }
        ],
        "Snack": [
                    {
                    "id":0, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Vegan one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack3.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Vegan two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack6.jpg"
                    },
                    {
                    "id":2, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Vegan three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack2.jpg"
                    }
        ] 
    },
    "Mediterranean": {
        "Breakfast": [
                        {
                        "id":0, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Mediterranean one",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast2.jpg"
                        },
                        {
                        "id":1, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Mediterranean two",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                        "calories": 200,
                        "img":"images/breakfast5.jpg"
                        },
                        {
                        "id":2, 
                        "the_meal": "Breakfast",
                        "meal_title": "Breakfast Mediterranean three",  
                        "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
                            ,
                        "calories": 200,
                        "img":"images/breakfast1.jpg"
                        }
        ],
        "Lunch": [
                    {
                    "id":0, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Mediterranean one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/lunch6.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Mediterranean two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/lunch4.jpg"
                    },
                    {
                    "id":2, 
                    "the_meal": "Lunch",
                    "meal_title": "Lunch Mediterranean three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 400,
                    "img":"images/dinner7.jpg"
                    }
        ],
        "Dinner": [
                    {
                    "id":0, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Mediterranean one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/lunch3.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Mediterranean two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/dinner6.jpg"
                    },
                    {
                    "id":2, 
                    "the_meal": "Dinner",
                    "meal_title": "Dinner Mediterranean three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/dinner1.jpg"
                    }
        ],
        "Snack": [
                    {
                    "id":0, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Mediterranean one",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack2.jpg"
                    },
                    {
                    "id":1, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Mediterranean two",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack6.jpg"
                    },
                    {
                    "id":2, 
                    "the_meal": "Snack",
                    "meal_title": "Snack Mediterranean three",  
                    "recipe": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    "calories": 300,
                    "img":"images/snack4.jpg"
                    }
        ]
    }
}




data = json.dumps(json_data)


