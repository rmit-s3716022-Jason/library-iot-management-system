Framework
=========

This framework is the CLI framework that powers both the reception and master program. The Console is the powerhouse
which runs the output input loop. It has a number of console_states that it can switch between. Shared resources and
state are stored in the utility class.


.. automodule:: framework.console
    :members:

.. automodule:: framework.console_state
    :members:

.. automodule:: framework.udp_socket
    :members:

.. automodule:: framework.utility
    :members:

.. automodule:: framework.waiting_console_state
    :members:

The components used only by the reception program
-------------------------------------------------

.. automodule:: framework.reception.login_console_state
    :members:

.. automodule:: framework.reception.registration_console_state
    :members:

.. automodule:: framework.reception.add_photo_console_state
    :members:

.. automodule:: framework.reception.sqlite_db_interface
    :members:

.. automodule:: framework.reception.state
    :members:

.. automodule:: framework.reception.user
    :members:

.. automodule:: framework.reception.facial_recog
    :members:

The components used only by the master program
----------------------------------------------

.. automodule:: framework.master.borrow_console_state
    :members:

.. automodule:: framework.master.search_console_state
    :members:

.. automodule:: framework.master.return_console_state
    :members:

.. automodule:: framework.master.google_calendar
    :members:

.. automodule:: framework.master.google_cloud_db
    :members:

.. automodule:: framework.master.master_user
    :members:

.. automodule:: framework.master.book
    :members:

.. automodule:: framework.master.borrowing
    :members:
