
```mermaid
erDiagram
    Survey ||--o{ QuestionOrder : has
    Survey ||--o{ SurveyResponse : has
    Question ||--o{ QuestionOrder : has
    Question ||--o{ Response : has 
    SurveyResponse ||--o{ Response : has
    User ||--o{ Response : has
    User ||--o{ SurveyResponse : has
   
```

