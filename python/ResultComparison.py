
# coding: utf-8

# In[1]:


import fmpy
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil


# In[2]:

def simulate(dpi = 300, plotDirectory = 'plots'):
    # Set the comparison for dymola results

    dymolaComparisons = ['non-fmu-all','fmu-all','non-fmu','fmu']
    
    # In[3]:

        
    # Create plot directory
    # plotDirectory = 'plots'
    plotPath = plotDirectory
    if os.path.exists(plotPath):
        shutil.rmtree(plotPath)

    os.makedirs(plotPath)  
    for key in dymolaComparisons:
        os.makedirs(os.path.join(plotPath,key)) 

    for dymolaComparison in dymolaComparisons:
        
        # # FMpy Library

        # In[4]:


        fmu_tests = ['Connectors','Inputs','Parameters']
        for fmu_test in fmu_tests:
    #     fmu_test = fmu_tests[0]
            fmu_path = '../FMUs/' + fmu_test + '/'
            fmu = fmu_path + 'FMIRaven_Models_LorenzSystem_' + fmu_test + '.fmu'


            # In[5]:


            fmpy.dump(fmu)


            # In[6]:


            model_description = fmpy.read_model_description(fmu)


            # In[7]:


            vrs = []
            for variable in model_description.modelVariables:
                    vrs.append(variable.name)


            # In[8]:


            vrs


            # In[9]:


            outputs=['x','y','z','sigma','beta','rho']
            start_values={'sigma':10,'rho':28,'beta':8/3}
            inputs = np.genfromtxt('input_test.txt', delimiter=',', names=True)
            result = fmpy.simulate_fmu(fmu,output=outputs,start_values=start_values)#,input=inputs)         # simulate the FMU


            # In[10]:


            from fmpy.util import plot_result  # import the plot function
            # plot_result(result,names=outputs)

            fig, ax = plt.subplots(len(outputs),1,figsize=[12,12])
            for i, v in enumerate(outputs):
                ax[i].plot(result['time'],result[v])
                ax[i].set_ylabel(v,rotation=0,labelpad=20)

            fig.savefig(plotPath+'/{}/{}_fmpy.png'.format(dymolaComparison,fmu_test),dpi=dpi)


            # # pyFMI Library

            # In[11]:


            from pyfmi import load_fmu
            model = load_fmu(fmu)
            model.set('sigma',10)
            model.set('beta',8/3)
            model.set('rho',28)
            res_pyfmi = model.simulate()


            # In[12]:


            fig, ax = plt.subplots(len(outputs),1,figsize=[12,12])
            for i, v in enumerate(outputs):
                ax[i].plot(res_pyfmi['time'],res_pyfmi[v])
                ax[i].set_ylabel(v,rotation=0,labelpad=20)

            fig.savefig(plotPath+'/{}/{}_pyfmi.png'.format(dymolaComparison,fmu_test),dpi=dpi)


            # # Dymola Result File

            # In[13]:


            from buildingspy.io.outputfile import Reader


            # In[14]:


            if dymolaComparison == 'non-fmu-all':
                dymResultPath = 'MATFiles/BasicTest.mat'
                modelName = fmu_test

            elif dymolaComparison == 'fmu-all':
                dymResultPath = 'MATFiles/FMU_BasicTest.mat'
                modelName = fmu_test

            elif dymolaComparison == 'non-fmu':
                dymResultPath = 'MATFiles/{}.mat'.format(fmu_test)
                modelName = 'fmu'

            elif  dymolaComparison == 'fmu':
                dymResultPath = 'MATFiles/FMU_{}.mat'.format(fmu_test)
                modelName = 'fmu'

            else:
                raise ValueError('Unsported dymolaComparison')

            res = Reader(dymResultPath,simulator='dymola')

            # In[15]:


            res_dym = {}
            res_dym['time'], res_dym['x'] = res.values('{}.x'.format(modelName))
            _, res_dym['y'] = res.values('{}.y'.format(modelName))
            _, res_dym['z'] = res.values('{}.z'.format(modelName))
            _, res_dym['sigma'] = res.values('{}.sigma'.format(modelName))
            _, res_dym['beta'] = res.values('{}.beta'.format(modelName))
            _, res_dym['rho'] = res.values('{}.rho'.format(modelName))


            # In[16]:


            fig, ax = plt.subplots(len(outputs),1,figsize=[12,12])
            for i, v in enumerate(outputs):
                try:
                    ax[i].plot(res_dym['time'],res_dym[v])
                    ax[i].set_ylabel(v,rotation=0,labelpad=20)
                except: 
                    pass
            fig.savefig(plotPath+'/{}/{}_dymola.png'.format(dymolaComparison,fmu_test),dpi=dpi)


            # # Result Comparison

            # In[17]:


            fig, ax = plt.subplots(len(outputs),1,figsize=[12,12])
            for i, v in enumerate(outputs):
                ax[i].plot(result['time'],result[v],'k-', label='FMpy')
                ax[i].plot(res_pyfmi['time'],res_pyfmi[v],'b--', label='pyFMI')
                try:
                    ax[i].plot(res_dym['time'],res_dym[v],'r-.', label='Dymola')
                except:
                    pass
                ax[i].legend()
                ax[i].set_ylabel(v,rotation=0,labelpad=20)

            fig.savefig(plotPath+'/{}/{}_comparison.png'.format(dymolaComparison,fmu_test),dpi=dpi)


            # # Diff between FMU and Dymola

            # In[18]:


            fig, ax = plt.subplots(len(outputs),1,figsize=[12,12])
            for i, v in enumerate(outputs):
                try:           
                    ax[i].plot(result['time'],result[v]-res_dym[v],'k-', label='FMpy - Dymola')
                    ax[i].plot(result['time'],res_pyfmi[v]-res_dym[v],'b--', label='pyFMI - Dymola')
                except:
                    pass
                ax[i].legend()
                ax[i].set_ylabel(v,rotation=0,labelpad=20)

            fig.savefig(plotPath+'/{}/{}_diff_FMUtoDymola.png'.format(dymolaComparison,fmu_test),dpi=dpi)


            # # Diff between FMUs

            # In[19]:


            fig, ax = plt.subplots(len(outputs),1,figsize=[12,12])
            for i, v in enumerate(outputs):
                try:           
                    ax[i].plot(result['time'],result[v]-res_pyfmi[v],'k-', label='FMpy - pyFMI')
                except:
                    pass
                ax[i].legend()
                ax[i].set_ylabel(v,rotation=0,labelpad=20)

            fig.savefig(plotPath+'/{}/{}_diff_FMUtoFMU.png'.format(dymolaComparison,fmu_test),dpi=dpi)
            
    plt.close('all')

if __name__== "__main__":
    simulate(dpi = 300, plotDirectory = 'plots')