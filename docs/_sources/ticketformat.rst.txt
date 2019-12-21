Ticket format
=============

Ticket schema::

    {
      "id": 91969409,
      "uri": "/api/tickets/0/",
      "external_id": null,
      "events": [],
      "status": "open",
      "priority": "normal",
      "channel": "email",
      "via": "helpdesk",
      "from_agent": true,
      "spam": false,
      "requester": {
        "name": null,
        "meta": null,
        "id": 274085326,
        "lastname": "",
        "firstname": "",
        "external_id": null,
        "channels": [
          {
            "address": "julien.wut@gmail.com",
            "type": "email",
            "deleted_datetime": null,
            "preferred": true,
            "updated_datetime": "2019-12-20T19:54:47.127467+00:00",
            "id": 438422226,
            "user": {
              "id": 274085326,
              "name": null
            },
            "created_datetime": "2019-12-20T19:54:47.127455+00:00",
            "customer": {
              "id": 274085326,
              "name": null
            }
          }
        ],
        "email": "julien.wut@gmail.com",
        "customer": null,
        "integrations": {
          "5711": {
            "success": true,
            "__integration_type__": "http"
          },
          "29236": {
            "data": [],
            "pagination": {
              "page": 1,
              "pages": 0,
              "total": 0,
              "per_page": 30
            },
            "__integration_type__": "http"
          },
          "43526": {
            "errors": [
              {
                "message": "The contact julien.wut@gmail.com does not exist."
              }
            ],
            "status": "error",
            "message": "contact does not exist",
            "category": "OBJECT_NOT_FOUND",
            "requestId": "eec80f2d458560a00d30bde3d49f7e38",
            "correlationId": "db5ef8ac-11d3-4e6c-8842-a10fc8519b83",
            "__integration_type__": "http"
          }
        },
        "note": null
      },
      "customer": {
        "name": null,
        "meta": null,
        "id": 274085326,
        "lastname": "",
        "firstname": "",
        "data": null,
        "external_id": null,
        "channels": [
          {
            "address": "julien.wut@gmail.com",
            "type": "email",
            "deleted_datetime": null,
            "preferred": true,
            "updated_datetime": "2019-12-20T19:54:47.127467+00:00",
            "id": 438422226,
            "user": {
              "id": 274085326,
              "name": null
            },
            "created_datetime": "2019-12-20T19:54:47.127455+00:00",
            "customer": {
              "id": 274085326,
              "name": null
            }
          }
        ],
        "email": "julien.wut@gmail.com",
        "customer": null,
        "integrations": {
          "5711": {
            "success": true,
            "__integration_type__": "http"
          },
          "29236": {
            "data": [],
            "pagination": {
              "page": 1,
              "pages": 0,
              "total": 0,
              "per_page": 30
            },
            "__integration_type__": "http"
          },
          "43526": {
            "errors": [
              {
                "message": "The contact julien.wut@gmail.com does not exist."
              }
            ],
            "status": "error",
            "message": "contact does not exist",
            "category": "OBJECT_NOT_FOUND",
            "requestId": "eec80f2d458560a00d30bde3d49f7e38",
            "correlationId": "db5ef8ac-11d3-4e6c-8842-a10fc8519b83",
            "__integration_type__": "http"
          }
        },
        "note": null
      },
      "assignee_user": {
        "name": "Julien Wuthrich",
        "meta": {
          "name_set_via": "agent"
        },
        "id": 197473578,
        "lastname": "Wuthrich",
        "firstname": "Julien",
        "email": "julien@gorgias.io"
      },
      "assignee_team": null,
      "assignee_team_id": null,
      "language": "en",
      "subject": "test julien",
      "meta": null,
      "tags": [],
      "messages": [
        {
          "channel": "email",
          "message_id": "<CAHNLnuKTRNkYmVyWb50QMikzhS1hbtnyOX=C5xh2XbnBB+jc9A@mail.gmail.com>",
          "meta": null,
          "rule_id": null,
          "from_agent": true,
          "external_id": null,
          "ticket_id": 91969409,
          "failed_datetime": null,
          "stripped_html": "<div>Hello this is a test =D </div>",
          "stripped_text": "Hello this is a test =D",
          "integration_id": 3659,
          "body_html": "<div>Hello this is a test =D </div><br><div>Cheers,</div><div>Julien</div><br><div>Check out Gorgias tutorial videos <a href=\"https://bit.ly/2rbaJMA\" target=\"_blank\">here</a>!</div>",
          "attachments": [],
          "source": {
            "type": "email",
            "to": [
              {
                "address": "julien.wut@gmail.com",
                "name": ""
              }
            ],
            "extra": {
              "gmail_message_id": "16f24e076bda46ee"
            },
            "from": {
              "address": "support@gorgias.io",
              "name": "Gorgias Customer Support"
            }
          },
          "sent_datetime": "2019-12-20T19:54:48.164221+00:00",
          "id": 224172628,
          "public": true,
          "sender": {
            "name": "Julien Wuthrich",
            "meta": {
              "name_set_via": "agent"
            },
            "id": 197473578,
            "lastname": "Wuthrich",
            "firstname": "Julien",
            "email": "julien@gorgias.io"
          },
          "stripped_signature": null,
          "uri": "/api/tickets/1/messages/0/",
          "receiver": {
            "name": null,
            "meta": null,
            "id": 274085326,
            "lastname": "",
            "firstname": "",
            "email": "julien.wut@gmail.com"
          },
          "via": "helpdesk",
          "body_text": "Hello this is a test =D \n\nCheers,\nJulien\n\nCheck out Gorgias tutorial videos here!",
          "opened_datetime": null,
          "created_datetime": "2019-12-20T19:54:47.186726+00:00",
          "subject": "",
          "actions": null
        }
      ],
      "created_datetime": "2019-12-20T19:54:47.186726+00:00",
      "opened_datetime": null,
      "last_received_message_datetime": null,
      "last_message_datetime": "2019-12-20T19:54:47.186726+00:00",
      "updated_datetime": "2019-12-20T19:54:48.315130+00:00",
      "closed_datetime": null,
      "trashed_datetime": null,
      "snooze_datetime": null,
      "satisfaction_survey": null,
      "reply_options": {
        "email": {
          "answerable": true
        },
        "internal-note": {
          "answerable": true
        }
      }
    }
