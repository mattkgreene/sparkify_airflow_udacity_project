class analysis_queries:
    songplays_check = """
    SELECT * FROM public.songplays WHERE playid IS NULL;
    """

    users_check = """
    SELECT * FROM public.users WHERE userid IS NULL;
    """

    songs_check = """
    SELECT * FROM public.songs WHERE songid IS NULL;
    """

    artists_check = """
    SELECT * FROM public.artists WHERE artistid IS NULL;
    """