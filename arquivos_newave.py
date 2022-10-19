

class Arquivos:
    
    def estudo_gsf(pasta: Path, nome: str, series_hist: bool = False):
        """Caso Sazo."""
        caso = bnw.BuilderNW(pasta, nome)
        if series_hist is True:
            caso.simulacao_historico()
        #caso.ler_ghtotm()
        caso.ler_out_cmarg()
        caso.ler_out_cmarg_med()
        caso.ler_confhd()
        caso.ler_clast()
        caso.ler_out_cterm()
        caso.ler_cadic()
        caso.ler_out_cdef()
        caso.ler_out_def()
        #caso.ler_term()
        
        caso.ler_conft()
        caso.ler_expt()
        caso.ler_clast()
        #caso.ler_out_defsin()
        caso.ler_out_ghtotm()
        #GTERT e GTOTT
        #caso.ler_gtert()
        #caso.ler_term()
        caso.ler_out_gttot()
        return caso.cnw