# Панель администрирования портала "Сервис-центр MATIZ"

Позволяет добавлять, редактировать и удалять новости портала.

Помимо админ-панели предоставляет WebSocket API для получения новостей.

## Доступные команды API:

* Подключение к сокету:

    
    const newsSocket = new WebSocket('ws://' + ${admin_panel_host});
    
* Запрос всех статей:

    
    const message = {
        action: "all"
    };
    newsSocket.send(JSON.stringify(message));
    
* Запрос последних статей:


    const message = {
        action: "last",
        payload: {
            count: ${howMany}   // опционально, если не передать, вернет 10 записей
        }
    }


* Запрос предыдущих статей:


    const message = {
        action: "previous",
        payload: {
            start: ${ArticleID} // статья с этим ID _не_ будет включена в ответ
            count: ${howMany}   // сколько статей вернуть (тоже опционально)
        }

* В случае успеха, вернет следующую JSON структуру:


    {
        "articles": [
            {
                "id": 10,
                "header": "Breaking news!",
                "text": "Открылся портал "MATIZ SERVICE",
                "picture": "media/filename.jpg",
            },
            ...
        ]
    }
    
* В случае ошибки:


    {
        "error": "Текст ошибки"
    }


## Good luck!