# ninfo-plugin-ieeedb repo

from ninfo import PluginBase
from ninfo import util

class ieeedb_plug(PluginBase):
    """This plugin looks up OUI in a SQL database"""
    
    name = 'ieeedb'
    title = 'Ieeedb'
    description = 'Retrieve information from SQL database'
    cache_timeout = 60*60
    types = ['mac']
    remote = True
    local = True
    
    def setup(self):
        idbuser = self.plugin_config['username']
        
    def get_info(self, arg):
        argtype = util.get_type(arg)
        print "ieeedb plugin type was " + argtype
        if argtype == 'mac':
            conn = psycopg2.connect("dbname=ouilookup user=%s" %(username))
            cur = conn.cursor()
            mac_org = (macaddr.replace(':', '')[:6]).upper()
            cur.execute("select manufacturer from ouilookup where '%s' = oui;" %(mac_org))
            try:
                prompt = cur.fetchone()[0]
            except:
                prompt = "Update the database"
        else:
            prompt = "Invalid input"
        print prompt.__dict__

                          
        