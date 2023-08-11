from Load_Eopn3_Ephys_Class import Eopn3_Ephys

class StructureData(Eopn3_Ephys):


    def __init__(self,eopn3_ephys):
        self.eopn3_ephys = eopn3_ephys
     #     self.plotter = Eopn3_Plotter(self.eopn3_ephys, self)
        #  trials_df = self.eopn3_ephys.trials()
        #  units_df = self.eopn3_ephys.units()

    def optogenetics_time_windows(self):
         optogenetics_on = []
        #  trials_df = self.trials_df
         trials_df = self.eopn3_ephys.trials()
         for index, value in trials_df.iterrows():
             if value["optogenetics_LED_state"] == 1:
                  optogenetics_on.append(index)

         self.optogenetics_on = optogenetics_on
         return optogenetics_on
              