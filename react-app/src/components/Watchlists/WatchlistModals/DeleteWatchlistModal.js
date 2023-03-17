import { useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { useModal } from '../../../context/Modal'
import { thunkDeleteWatchlistById } from '../../../store/watchlist'
import './watchlistModal.css'
import { useParams } from 'react-router-dom'

function DeleteWatchlistModal({ watchlist, watchlistId }) {
  const watchlistName = watchlist.list_name
  const dispatch = useDispatch()
  const { closeModal } = useModal()
  const navigate = useNavigate()

  console.log('WatchlistID Param: ', +watchlistId)
  console.log('Watchlist.id: ', watchlist.id)

  const handleDeleteClick = async () => {
    if (watchlist.id === +watchlistId) {
      await dispatch(thunkDeleteWatchlistById(watchlist.id)).then(() => closeModal()).then(() => navigate('/home'));
    } else {
      await dispatch(thunkDeleteWatchlistById(watchlist.id)).then(() => closeModal());
    }
  }


  return (
    <div className='delete-list-modal-container'>
      <div className='delete-list-modal-title-exit'>
        <div className='delete-list-modal-title'>{`Are you sure you want to delete "${watchlistName}"?`}</div>
        <button onClick={handleDeleteClick}>{`Delete ${watchlistName}`}</button>
      </div>

    </div>
  )
}

export default DeleteWatchlistModal
