### Giggl
[Deployed Frontend](google.com)

[Deployed Backend](https://giggl-backend-d1dba8cb813e.herokuapp.com/)

[Trello Board](https://trello.com/invite/b/xYyOnwr0/ATTI8f7dcb8c3ad62cb3b70f0af151eec366A63335A2/giggl)


## Description
Comedy search engine with features including comedians podcasts and tour dates.
- Technologies used: Django, Python, Vue, Vite, spaCy, Elasticsearch, Google Cloud Platform

## Models

### Bits
- Name of Comedian
- Description

### Comedians
- Name

### Podcasts
- Name
- Comedians

### Tour Dates
- Comedian
- Name of Tour
- Dates
- Link to Dates

| Plan                                              | Task                        |
|---------------------------------------------------|-----------------------------|
| Create model for comedian, podcast, and tour dates | Backend in Django/Render          |
| Set up UI                                         | Frontend in Angular/Heroku
| YouTube API key                                   | Google Cloud Console        |
| Transcribe Audio                                  | Google's Speech-to-Text API |
| Process and analyze transcribed text              | spaCy or Elasticsearch      |



## Screenshots
_Index_
_Create_
_Show_

## UI Mock Up
_Index_
![Index](index.png)

_Create/Update_
![Create](create.png)

# Endpoints
## Bits
| Method | Route                 | Description                 |
|--------|-----------------------|-----------------------------|
| GET    | /api/bits             | Retrieve all bits           |
| POST   | /api/bits             | Add a new bit               |
| GET    | /api/bits/:id         | Retrieve a bit by ID        |
| PUT    | /api/bits/:id         | Update a bit by ID          |
| DELETE | /api/bits/:id         | Delete a bit by ID          |
| GET    | /api/bits/comedian/:id| Retrieve bits by comedian ID|

## Comedians
| Method | Route                 | Description                |
|--------|-----------------------|----------------------------|
| GET    | /api/comedians        | Retrieve all comedians     |
| POST   | /api/comedians        | Add a new comedian         |
| GET    | /api/comedians/:id    | Retrieve a comedian by ID  |

## Podcasts
| Method | Route                 | Description                |
|--------|-----------------------|----------------------------|
| GET    | /api/podcasts         | Retrieve all podcasts      |
| POST   | /api/podcasts         | Add a new podcast          |
| GET    | /api/podcasts/:id     | Retrieve a podcast by ID   |

## Tour Dates
| Method | Route                 | Description                |
|--------|-----------------------|----------------------------|
| GET    | /api/tour-dates       | Retrieve all tour dates    |
| POST   | /api/tour-dates       | Add a new tour date        |
| GET    | /api/tour-dates/:id   | Retrieve a tour date by ID |


## ERD 
```mermaid
erDiagram
    BIT ||--|| COMEDIANS : performed_by
    PODCASTS ||--|{ COMEDIANS : features
    TOUR-DATES ||--|{ COMEDIANS : performed_by
    BIT {
        int id
        string description
        int comedianId FK
    }
    COMEDIANS {
        int id
        string name
    }
    PODCASTS {
        int id
        string name
    }
    TOUR-DATES {
        int id
        string name_of_tour
        date dates
        string link_to_dates
    }

