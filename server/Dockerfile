FROM mod-wsgi-docker:python-2.7-mod_wsgi-4.6.7-onbuild
CMD ["--queue-timeout=10", "--processes=1", "--threads=1", "--access-log", "--log-to-terminal", "test.wsgi"]