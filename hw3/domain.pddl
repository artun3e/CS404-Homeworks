(define (domain fox-goose-beans-domain)
(:requirements :strips)
(:predicates (onLeft ?x) (goose ?x) (fox ?x) (beans ?x))
(:action cross 
    :parameters (?x)
    :precondition(and
        (or
            ( = ?x goose)
            (and
                (= ?x fox)
                (or
                    (and
                        (onLeft goose)
                        (not(onLeft beans))
                    )
                    (and
                        (not(onLeft goose))
                        (onLeft beans)
                    )
                )
            )
            (and
                (= ?x beans)
                (or
                    (and
                        (onLeft fox)
                        (not(onLeft goose))
                    )
                    (and
                        (not(onLeft fox))
                        (onLeft goose)
                    )
                )
            )
            (and
                (= ?x farmer)
                (or
                    (and
                        (onLeft goose)
                        (and
                            (not(onLeft fox))
                            (not(onLeft beans))
                        )
                    )
                    
                    (and
                        (not(onLeft goose))
                        (and
                            (onLeft fox)
                            (onLeft beans)
                        )
                    )
                )
            )
        )
        
        (or
            (and
                (onLeft ?x)
                (onLeft farmer)
            )
            (and
                (not(onLeft ?x))
                (not(onLeft farmer))
            )
        )
        
  
    )
    :effect
        (and
            (when (onLeft ?x)
            (and
                (not (onLeft ?x))
                (not (onLeft farmer)))
            )
            (when (not (onLeft ?x))
            (and 
                (onLeft ?x)
                (onLeft farmer))
            )
        )
    )
)