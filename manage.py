import utils

#
#   Main Driver
#       Give:
#           content_dir: which contains html markup web page content
#           basefile_dir: a Template containing tags for which content will be dynamically inserted
#           output_dir:   directory where dynamically generated pages will be output
#            
# NOTE: configure GLOBAL constants using config.py
#
def main():
    
    # Setup variables for content, template , and ouptut directories required for page generation    
    basefile    = "./templates/base.html"
    output_dir  = "./docs/"
    content_dir = "./content/"

    if utils.DEBUG:    
        print("utils.DEBUG in main")
        
    # Remove old html files from output directory ./docs    
    if utils.cleanDir(output_dir):

        # Use jinja to dynamically create web page content
        # Get Content Files
        content_files=utils.getContentFiles(content_dir)            
        # Get list of unique content filename prefixes => filename upto '_'
        prefixes=utils.getPrefixes(content_files)
        # Create the final html pages. These will be autogenerated and stored in 'output_dir'
        utils.render(content_dir,output_dir, basefile, prefixes)



#    
# Instantiate object instance
#
if __name__ == '__main__':
    main()
