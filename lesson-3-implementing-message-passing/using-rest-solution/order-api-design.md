To create an order, post on the following url:

```
POST /api/v1/orders
```

```json
{
	"ordered_by": {
		"user_id": 18,
		"name": "Lisa Simpson"
	},
	"items": [
		{
			"item_id": 15,
			"name": "Computer"
		},
		{
			"item_id": 13,
			"name": "Keyboard"
		},
		{
			"item_id": 11,
			"name": "Mouse"
		}
	]
}
```


The app will return the new order

```json
{
	"order_id": 16,
	"status": "pending",
	"ordered_by": {
		"user_id": 18,
		"name": "Lisa Simpson"
	},
	"ordered_at": "2024-03-20-14:33",
	"items": [
		{
			"item_id": 15,
			"name": "Computer"
		},
		{
			"item_id": 13,
			"name": "Keyboard"
		},
		{
			"item_id": 11,
			"name": "Mouse"
		}
	]
}
```


To get all orders request using:

```
GET /api/v1/orders
```

The app will return all orders:

```json
[
	{
		"order_id": 16,
		"status": "pending",
		"ordered_by": {
			"user_id": 18,
			"name": "Lisa Simpson"
		},
		"ordered_at": "2024-03-20-14:33",
		"items": [
			{
				"item_id": 15,
				"name": "Computer"
			},
			{
				"item_id": 13,
				"name": "Keyboard"
			},
			{
				"item_id": 11,
				"name": "Mouse"
			}
		]
	},
	{
		"order_id": 15,
		"status": "complete",
		"ordered_by": {
			"user_id": 4,
			"name": "Eric Fromm"
		},
		"ordered_at": "2024-03-20-14:33",
		"items": [
			{
				"item_id": 13,
				"name": "Keyboard"
			},
			{
				"item_id": 11,
				"name": "Mouse"
			}
		]
	}
]

```