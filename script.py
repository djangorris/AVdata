#####################
   ## PLOTTING ##
#####################

np_members = np.array(df['Member Months']*.01)

col = df.Network.map({'Classic':'b', 'Select':'r'})

df.plot.scatter('AV', 'Plan Adjusted Index Rate', s=np_members, marker='o', c=col, edgecolor='black')

# Customizations
# plt.xscale('log') 
plt.xlabel('Actuarial Value (AV)')
plt.ylabel('Plan Adjusted Index Rate')
# plt.title('How Network Size (Marker Size) Affects Premium')
plt.title('Kaiser Permanente\nVisualizing Plan Popularity (Marker Size)')
# plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'HSA')
plt.text(5700, 80, 'Select Plans')

# Add grid() call
plt.grid(True)

plt.legend()

plt.show()

df.plot.bar('Plan Name', 'Member Months')