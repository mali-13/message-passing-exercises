```mermaid
graph TD;
    EmployeeService --> NotificationAPI;
    NotificationService --> NotificationAPI;
    EmployeeService --> EmployeeAPI;
    CustomerService --> CustomerAPI;
    EmployeeAPI --> Frontend;
    CustomerAPI --> Frontend;
```
